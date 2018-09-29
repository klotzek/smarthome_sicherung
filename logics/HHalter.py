#!/usr/bin/env python3
logger.info ("Logik Boost Handtuchhalter wurde getriggert")

if sh.EG.Duschen.Heizung.boost_hhalter(): 
  time.sleep(1800)
  sh.EG.Duschen.Heizung.boost_hhalter(0)
  