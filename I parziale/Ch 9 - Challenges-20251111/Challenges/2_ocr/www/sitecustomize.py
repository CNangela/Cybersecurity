# sitecustomize.py
# Compat layer per Python >= 3.12: fornisce distutils.version.LooseVersion se mancante.
import sys
import types

try:
    # Se esiste già (es. ambienti particolari), non fare nulla
    import distutils.version  # type: ignore
except Exception:
    try:
        from packaging.version import Version as _Version
    except Exception:  # packaging non disponibile? poco probabile ma gestiamo
        class _Version:
            def __init__(self, v): self._v = str(v)
            def __str__(self): return self._v
            def __repr__(self): return f"Version('{self._v}')"
            def _cmp_tuple(self):  # confronto naive
                return tuple(int(p) if p.isdigit() else p for p in self._v.replace('-', '.').split('.'))
            def __lt__(self, other): return self._cmp_tuple() < other._cmp_tuple()
            def __le__(self, other): return self._cmp_tuple() <= other._cmp_tuple()
            def __eq__(self, other): return self._cmp_tuple() == other._cmp_tuple()
            def __ne__(self, other): return self._cmp_tuple() != other._cmp_tuple()
            def __gt__(self, other): return self._cmp_tuple() > other._cmp_tuple()
            def __ge__(self, other): return self._cmp_tuple() >= other._cmp_tuple()

    distutils_mod = types.ModuleType("distutils")
    distutils_ver_mod = types.ModuleType("distutils.version")

    class LooseVersion:
        """Compatibile con l'uso tipico: confronto di versioni."""
        def __init__(self, v): self._v = _Version(str(v))
        def __str__(self): return str(self._v)
        def __repr__(self): return f"LooseVersion('{self._v}')"
        def __lt__(self, other): return self._v < other._v
        def __le__(self, other): return self._v <= other._v
        def __eq__(self, other): return self._v == other._v
        def __ne__(self, other): return self._v != other._v
        def __gt__(self, other): return self._v > other._v
        def __ge__(self, other): return self._v >= other._v

    distutils_ver_mod.LooseVersion = LooseVersion
    sys.modules["distutils"] = distutils_mod
    sys.modules["distutils.version"] = distutils_ver_mod
