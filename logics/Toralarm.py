#!/usr/bin/env python3
logger.info ("Logik Toralarm wurde getriggert")

Tor1 = 0
Tor2 = 0
Tor3 = 0

if not sh.EG.Oekonomie.Scheunentor.Tor_Status():
  logger.info("Scheunentor offen (Status=0)")
  Tor1 = 1
  
if not sh.EG.Oekonomie.Scheunentor_Zirell.Tor_Status():
    logger.info("Scheunentor Zirell offen (Status 0)")
    Tor2 = 1

if not sh.EG.Oekonomie.Scheunentor_Berthold.Tor_Status():
    logger.info("Scheunentor Berthold offen (Status 0)")
    Tor3 = 1

if Tor1 or Tor2 or Tor3:
    logger.info("Eines der Tore steht offen")
    sh.EG.Oekonomie.Toralarm(1)
    sh.EG.Oekonomie.Licht_Scheune.Schalten(1)
else:
    logger.info("Alle Tore sind geschlossen")
    sh.EG.Oekonomie.Toralarm(0)
    time.sleep(180)
    sh.EG.Oekonomie.Licht_Scheune.Schalten(0)
