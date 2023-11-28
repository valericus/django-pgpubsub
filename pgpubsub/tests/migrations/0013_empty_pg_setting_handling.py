# Generated by Django 3.2.12 on 2023-11-28 09:15

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0012_payload_context'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='author',
            name='pgpubsub_160cf',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='child',
            name='pgpubsub_89ef9',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='childofabstract',
            name='pgpubsub_b1c0b',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='media',
            name='pgpubsub_a83de',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='post',
            name='pgpubsub_72091',
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='author',
            trigger=pgtrigger.compiler.Trigger(name='pgpubsub_160cf', sql=pgtrigger.compiler.UpsertTriggerSql(declare='DECLARE payload JSONB; notification_context JSONB; notification_context_text TEXT;', func='\n            \n            payload := \'{"app": "tests", "model": "Author"}\'::jsonb;\n            payload := jsonb_insert(payload, \'{old}\', COALESCE(to_jsonb(OLD), \'null\'));\n            payload := jsonb_insert(payload, \'{new}\', COALESCE(to_jsonb(NEW), \'null\'));\n            SELECT current_setting(\'pgpubsub.notification_context\', True) INTO notification_context_text;\n            IF COALESCE(notification_context_text, \'\') = \'\' THEN\n                notification_context_text := \'{}\';\n            END IF;\n            payload := jsonb_insert(payload, \'{context}\', notification_context_text::jsonb);\n        \n            \n            INSERT INTO pgpubsub_notification (channel, payload)\n            VALUES (\'pgpubsub_160cf\', payload);\n        \n            perform pg_notify(\'pgpubsub_160cf\', payload::text);\n            RETURN NEW;\n        ', hash='a0cc1827e0c0c6faef61951e3494bbe69a8448ed', operation='INSERT', pgid='pgtrigger_pgpubsub_160cf_72a36', table='tests_author', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='child',
            trigger=pgtrigger.compiler.Trigger(name='pgpubsub_89ef9', sql=pgtrigger.compiler.UpsertTriggerSql(declare='DECLARE payload JSONB; notification_context JSONB; notification_context_text TEXT;', func='\n            \n            payload := \'{"app": "tests", "model": "Child"}\'::jsonb;\n            payload := jsonb_insert(payload, \'{old}\', COALESCE(to_jsonb(OLD), \'null\'));\n            payload := jsonb_insert(payload, \'{new}\', COALESCE(to_jsonb(NEW), \'null\'));\n            SELECT current_setting(\'pgpubsub.notification_context\', True) INTO notification_context_text;\n            IF COALESCE(notification_context_text, \'\') = \'\' THEN\n                notification_context_text := \'{}\';\n            END IF;\n            payload := jsonb_insert(payload, \'{context}\', notification_context_text::jsonb);\n        \n            \n            INSERT INTO pgpubsub_notification (channel, payload)\n            VALUES (\'pgpubsub_89ef9\', payload);\n        \n            perform pg_notify(\'pgpubsub_89ef9\', payload::text);\n            RETURN NEW;\n        ', hash='cec5f55510398cb434023b5ac3d4c0795e0fd480', operation='UPDATE OR INSERT', pgid='pgtrigger_pgpubsub_89ef9_92bc1', table='tests_child', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='childofabstract',
            trigger=pgtrigger.compiler.Trigger(name='pgpubsub_b1c0b', sql=pgtrigger.compiler.UpsertTriggerSql(declare='DECLARE payload JSONB; notification_context JSONB; notification_context_text TEXT;', func='\n            \n            payload := \'{"app": "tests", "model": "ChildOfAbstract"}\'::jsonb;\n            payload := jsonb_insert(payload, \'{old}\', COALESCE(to_jsonb(OLD), \'null\'));\n            payload := jsonb_insert(payload, \'{new}\', COALESCE(to_jsonb(NEW), \'null\'));\n            SELECT current_setting(\'pgpubsub.notification_context\', True) INTO notification_context_text;\n            IF COALESCE(notification_context_text, \'\') = \'\' THEN\n                notification_context_text := \'{}\';\n            END IF;\n            payload := jsonb_insert(payload, \'{context}\', notification_context_text::jsonb);\n        \n            \n            INSERT INTO pgpubsub_notification (channel, payload)\n            VALUES (\'pgpubsub_b1c0b\', payload);\n        \n            perform pg_notify(\'pgpubsub_b1c0b\', payload::text);\n            RETURN NEW;\n        ', hash='70a23861f292d3be26d11f30fbbca98b781e5d57', operation='UPDATE OR INSERT', pgid='pgtrigger_pgpubsub_b1c0b_c8531', table='tests_childofabstract', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='media',
            trigger=pgtrigger.compiler.Trigger(name='pgpubsub_a83de', sql=pgtrigger.compiler.UpsertTriggerSql(declare='DECLARE payload JSONB; notification_context JSONB; notification_context_text TEXT;', func='\n            \n            payload := \'{"app": "tests", "model": "Media"}\'::jsonb;\n            payload := jsonb_insert(payload, \'{old}\', COALESCE(to_jsonb(OLD), \'null\'));\n            payload := jsonb_insert(payload, \'{new}\', COALESCE(to_jsonb(NEW), \'null\'));\n            SELECT current_setting(\'pgpubsub.notification_context\', True) INTO notification_context_text;\n            IF COALESCE(notification_context_text, \'\') = \'\' THEN\n                notification_context_text := \'{}\';\n            END IF;\n            payload := jsonb_insert(payload, \'{context}\', notification_context_text::jsonb);\n        \n            \n            INSERT INTO pgpubsub_notification (channel, payload)\n            VALUES (\'pgpubsub_a83de\', payload);\n        \n            perform pg_notify(\'pgpubsub_a83de\', payload::text);\n            RETURN NEW;\n        ', hash='e2105ac0a63a4c12537a35577d6bf396d256e6db', operation='UPDATE OR INSERT', pgid='pgtrigger_pgpubsub_a83de_cacbb', table='tests_media', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='post',
            trigger=pgtrigger.compiler.Trigger(name='pgpubsub_72091', sql=pgtrigger.compiler.UpsertTriggerSql(declare='DECLARE payload JSONB; notification_context JSONB; notification_context_text TEXT;', func='\n            \n            payload := \'{"app": "tests", "model": "Post"}\'::jsonb;\n            payload := jsonb_insert(payload, \'{old}\', COALESCE(to_jsonb(OLD), \'null\'));\n            payload := jsonb_insert(payload, \'{new}\', COALESCE(to_jsonb(NEW), \'null\'));\n            SELECT current_setting(\'pgpubsub.notification_context\', True) INTO notification_context_text;\n            IF COALESCE(notification_context_text, \'\') = \'\' THEN\n                notification_context_text := \'{}\';\n            END IF;\n            payload := jsonb_insert(payload, \'{context}\', notification_context_text::jsonb);\n        \n            \n            INSERT INTO pgpubsub_notification (channel, payload)\n            VALUES (\'pgpubsub_72091\', payload);\n        \n            perform pg_notify(\'pgpubsub_72091\', payload::text);\n            RETURN NEW;\n        ', hash='132438a8b48b5ee1766405ca35a1f32895eda92d', operation='DELETE', pgid='pgtrigger_pgpubsub_72091_67aeb', table='tests_post', when='AFTER')),
        ),
    ]
