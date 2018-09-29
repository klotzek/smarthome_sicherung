#!/usr/bin/env python3
logger.info ("Sonnen- und Mond-Aufgangs- und Untergangszeiten werden berechnet")
sh.system.datum_uhrzeit.sonne.aufgang(sh.env.location.sunrise())
sh.system.datum_uhrzeit.sonne.untergang(sh.env.location.sunset())
sh.system.datum_uhrzeit.mond.aufgang(sh.env.location.moonrise())
sh.system.datum_uhrzeit.mond.untergang(sh.env.location.moonset())

