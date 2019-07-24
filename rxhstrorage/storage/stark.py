from stark.service.stark import site, StarkConfig, Option, url
from storage import models


class MaterialCofig(StarkConfig):

    #复选框
    list_display = [StarkConfig.display_checkbox,'id', 'name', 'amount', 'update_data', 'storage', 'pos', 'cls']

    list_filter = [
        Option('storage', is_multi=True),
        Option('pos', is_multi=True),
        Option('cls', is_multi=True),
    ]

    search_list = ['name']

    #批量删除
    action_list = [StarkConfig.multi_delete, ]


site.register(models.Material, MaterialCofig)


class PosConfig(StarkConfig):
    list_display = ['id', 'name', ]

    def get_urls(self):
        urlpatterns = [
            url(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            url(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            url(r'^(?P<pk>\d+)/change/', self.wrapper(self.change_view), name=self.get_change_url_name),
            # url(r'^(?P<pk>\d+)/del/', self.wrapper(self.delete_view), name=self.get_del_url_name),
        ]

        extra = self.extra_url()
        if extra:
            urlpatterns.extend(extra)

        return urlpatterns

    def get_list_display(self):
        val = []
        val.extend(self.list_display)
        val.append(StarkConfig.display_edit_del('edit'))
        return val


site.register(models.Position, PosConfig)


class StorageRackConfig(StarkConfig):
    list_display = ['id', 'num', ]

    def get_urls(self):
        urlpatterns = [
            url(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            url(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            url(r'^(?P<pk>\d+)/change/', self.wrapper(self.change_view), name=self.get_change_url_name),
            # url(r'^(?P<pk>\d+)/del/', self.wrapper(self.delete_view), name=self.get_del_url_name),
        ]

        extra = self.extra_url()
        if extra:
            urlpatterns.extend(extra)

        return urlpatterns

    def get_list_display(self):
        val = []
        val.extend(self.list_display)
        val.append(StarkConfig.display_edit_del('edit'))
        return val


site.register(models.StorageRack, StorageRackConfig)


class MaterialClsConfig(StarkConfig):
    list_display = ['id', 'name']


site.register(models.MaterialCls, MaterialClsConfig)
