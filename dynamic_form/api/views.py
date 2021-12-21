from bson.objectid import ObjectId
import csv
import io
import json
from bson import json_util

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.http import QueryDict

from api.models import Form, Response, Field


# Create your views here.
def index(request):
    return render(request, "index.html")


@method_decorator(csrf_exempt, name='dispatch')
class FormView(View):
    def get(self, request, form_id):
        form = Form.objects.get(_id=ObjectId(form_id))
        form_data = dict(
            form_id=str(form._id), form_name=form.name,
            fields=json_util.dumps(form.fields)
        )
        return JsonResponse(form_data)

    def post(self, request, form_id=None):
        form_name = request.POST.get("form_name")
        csvfile = request.FILES.get("csv_file")
        try:
            csvfile.seek(0)
            reader = csv.DictReader(io.StringIO(csvfile.read().decode('utf-8')))
            fields = []
            for row in reader:
                row["_id"] = ObjectId()
                fields.append(row)
            if form_id is None:
                form = Form.objects.create(name=form_name, fields=fields)
            else:
                form = Form.objects.get(_id=ObjectId(form_id))
                form.name = form_name
                form.fields.extend(fields)
                form.save()
            form_data = dict(
                form_id=str(form._id), form_name=form.name,
                fields=json_util.dumps(form.fields)
            )
            context = {"status": "success", "form_data": form_data}
        except Exception as e:
            context = {"status": "failed"}
        return JsonResponse(context)

    def delete(self, request, form_id):
        form = Form.objects.get(_id=ObjectId(form_id))
        field_ids = [str(field.get("_id")) for field in form.fields]
        for field_id in field_ids:
            Fields.objects.get(_id=ObjectId(field_id)).delete()
        form.delete()
        return JsonResponse({"status": "deleted"})


@method_decorator(csrf_exempt, name='dispatch')
class ResponseView(View):
    def get(self, request, response_id):
        response = Response.objects.get(_id=ObjectId(response_id))
        response_data = dict(form_id=str(response.form._id), answers=response.answers)
        return JsonResponse(form_data)

    def post(self, request, form_id):
        answers = request.POST.get("answers")
        form = Form.objects.get(_id=ObjectId(form_id))
        form = model_to_dict(form)
        response = Response.objects.create(form=form, answers=json_util.loads(answers))
        response_data = dict(
            response_id=str(response._id), form_id=form_id,
            answers=response.answers
        )
        return JsonResponse({"message": "success", "response": response_data})

