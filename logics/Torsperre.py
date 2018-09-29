#!/usr/bin/env python3
logger.info ("Logik Torsperre wurde getriggert")

sh.EG.Oekonomie.Scheunentor.Sperre(1)
time.sleep(300)
sh.EG.Oekonomie.Scheunentor.Sperre(0)
  