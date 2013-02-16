# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Passport.annotation'
        db.delete_column('core_passport', 'annotation')


    def backwards(self, orm):
        # Adding field 'Passport.annotation'
        db.add_column('core_passport', 'annotation',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    models = {
        'core.passport': {
            'Meta': {'object_name': 'Passport'},
            'army': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'children': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '255'}),
            'date_of_list': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_of_service_expired': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'education_type': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'employment_place': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fact_live_address_in_mo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fact_live_address_outside_mo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'family_status': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'form_of_care': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'has_real_estate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_institution_of_education': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'no_reqistration_reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'place_of_first_find': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'provision_of_employment_type': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'real_estate_EGRP': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'real_estate_not_EGRP': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registration_type': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'reqistration_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spokesman_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vacation': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['core']