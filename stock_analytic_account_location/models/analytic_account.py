# -*- coding: utf-8 -*-
# © 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp.osv import fields, orm


class AccountAnalyticAccount(orm.Model):
    _inherit = 'account.analytic.account'

    def _check_location(self, cr, uid, ids, context=None):
        for analytic in self.browse(cr, uid, ids):
            if analytic.location_id:
                if analytic.location_id.analytic_account_id != analytic:
                    return False
        return True

    _constraints = [(_check_location, "The location does not belong to this "
                                      "project",
                     ['analytic_account_id'])]
