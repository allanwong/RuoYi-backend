# Create your views here.
from django.http import FileResponse, Http404

from crud_demo.models import CrudDemoModel
from crud_demo.serializers import CrudDemoModelSerializer, CrudDemoModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class CrudDemoModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = CrudDemoModel.objects.all()
    serializer_class = CrudDemoModelSerializer
    create_serializer_class = CrudDemoModelCreateUpdateSerializer
    update_serializer_class = CrudDemoModelCreateUpdateSerializer
    filter_fields = ['goods', 'goods_price']
    search_fields = ['goods']

    # 分析结果 下载
    def Download(self, request):
        try:
            response = FileResponse(open('./media/data/classifyResults.json', 'rb'))
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=classifyResults.json'
            return response
        except Exception:
            raise Http404