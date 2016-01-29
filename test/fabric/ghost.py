import re

from fabric.api import env, run, hide, task
from envassert import detect, file, package, port, process, service, user
from hot.utils.test import get_artifacts

@task
def check():
    env.platform_family = detect.detect()

    assert port.is_listening(2368), 'port 2368/ghost is not listening'
    assert port.is_listening(80), 'port 80/nginx is not listening'
    assert port.is_listening(443), 'port 443/nginx is not listening'

    assert process.is_up('node'), 'node/ghost is not running'
    assert service.is_enabled('nginx'), 'nginx is not enabled'

    assert process.is_up('nginx'), 'nginx is not running'

@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
