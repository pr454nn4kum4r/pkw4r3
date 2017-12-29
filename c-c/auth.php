<?php
/* 
Authentication mechanism: 
1) Check id auth_code (jazbqw) is of 32 characters;
2) Check if 10-11 characters are divisible by 3;
3) check if 23-24 characters are divisible by 5;
*/
function check_authcode($auth_code){
	$auth_code_length = strlen($auth_code);

if(($auth_code_length>=25)&&($auth_code_length<=55)){

	

	$first_check_pos = floor($auth_code_length/2);
	$second_check_pos = floor($auth_code_length/4);


	$first_check_num = substr($auth_code, $first_check_pos, 2);
	$second_check_num = substr($auth_code, $second_check_pos, 2);

	if(($first_check_num%5===0)&&($second_check_num%3===0)){
		return "you_are_your_mothers_trueborn_son_of_lannister";
	}

	else{
	return "What_do_we_say_to_Lord_of_Death_Not_Today";
}
	
	}

}
?>