#
# ovirt-engine-setup -- ovirt engine setup
#
# Copyright oVirt Authors
# SPDX-License-Identifier: Apache-2.0
#
#


from otopi import util


from . import connection
from . import engine_connection
from . import pgpass


@util.export
def createPlugins(context):
    connection.Plugin(context=context)
    engine_connection.Plugin(context=context)
    pgpass.Plugin(context=context)

# vim: expandtab tabstop=4 shiftwidth=4
