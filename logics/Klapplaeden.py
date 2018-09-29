#!/usr/bin/env python3

now = sh.now()
vormittag = now.hour < 12
logger.info("Logik Klapplaeden gestartet")
        
if sh.now().weekday() in [0,1,2,3,4]:
        logger.info("Setzte den Klapplaeden Sheduler auf Wochentag")
        if vormittag:
          sh.Szene_Klapplaeden(0)
          logger.info("Klapplaeden auf")
else:
  if vormittag:
    if now.hour > 8:
          sh.Szene_Klapplaeden(0)
          logger.info("Klapplaeden auf Wochenende")
    

if not vormittag:
  sh.Szene_Klapplaeden(1)
  logger.info("Klapplaeden zugefahren")
  