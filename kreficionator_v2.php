<?php

/*
https://youtu.be/5YO7Vg1ByA8
https://onlinephp.io/
['s', 'ss', 'c', 'ç', 'sc', 't', 'x', 'z', 'th', 'sth', 'cc', 'sç']
*/

$counter = 0;
foreach (['k', 'c', 'ch', 'q'] as $k) {
  foreach (['r'] as $r) {
    foreach (['ai', 'è'] as $ai) {
      foreach (['f', 'ff', 'ph'] as $f) {
        foreach (['i', 'y'] as $y) {
          foreach (['s', 'ss', 'c', 'ç', 'sc', 't', 'x', 'z', 'th', 'sth', 'cc', 'sç'] as $s) {
            foreach (['i', 'y'] as $i) {
              foreach (['on', 'ond', 'ont'] as $on) {
                $result = $k.$r.$ai.$f.$y.$s.$i.$on;
                if (!preg_match('/ffy|fy|tiond|tiont/', $result)) {
                  echo sprintf("%4d. ", ++$counter) . preg_replace('/èff/', 'eff', $result) . "\n";
                }
              }
            }
          }
        }
      }
    }
  }
}
?>
