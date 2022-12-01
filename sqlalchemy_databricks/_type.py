from pyhive.sqlalchemy_hive import HiveTypeCompiler


class DatabricksTypeCompiler(HiveTypeCompiler):

    def visit_NUMERIC(self, type_):
        precision = getattr(type_, "precision", None)
        if precision is None:
            return "DECIMAL"
        else:
            scale = getattr(type_, "scale", None)
            if scale is None:
                return "DECIMAL(%(precision)s)" % {"precision": precision}
            else:
                return "DECIMAL(%(precision)s, %(scale)s)" % {"precision": precision, "scale": scale}

    def visit_DATE(self, type_):
        # Woraround because pyhive uses TIMESTAMP instead of DATE.
        # See as well: https://github.com/dropbox/PyHive/issues/139
        return 'DATE'
