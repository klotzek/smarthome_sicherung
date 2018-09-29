#!/usr/bin/env python3
if not sh.EG.Oekonomie.Scheunentor.Tor_Status():
  logger.info("Scheunentor offen (Status=0)")
  
  if sh.EG.Oekonomie.Scheunentor.Automatik():
    if not sh.EG.Oekonomie.Scheunentor.Sperre():
      sh.EG.Oekonomie.Scheunentor.Bewegen(1)
      logger.info("Scheunentor gefahren")
    else:
      logger.info("Sperre aktiv!")
  else:
    logger.info("Automatik aus")

else:
  logger.info("Scheunentor geschlossen (Status=1)")
  