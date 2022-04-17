from django.db import models
from django.db.models import CharField


class WorkerReplicaManager(models.Manager):
    def get_queryset(self):
        """
        Return a new QuerySet object. Subclasses can override this method to
        customize the behavior of the Manager.
        """
        return super().get_queryset().using('replica')


class Worker(models.Model):
    """
    Воркеры
    """

    name = CharField('Имя', max_length=64)

    objects = models.Manager()
    from_replica = WorkerReplicaManager()

    class Meta:
        db_table = 'worker'


