<?php
$username='DREAMWAVE';
$password='Dreamwave1234';
$URL='https://rby-ua.deposco.com/integration/rby/items/';
$data = '
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns2:items xmlns:ns2="http://integration.deposco.com/item">
    <item>
        <businessUnit>RBY</businessUnit>
        <number>190071</number>
        <name>190071</name>
        <shortDescription>CAT Master UENG (EA)</shortDescription>
        <longDescription>CAT Master UENG (EA)</longDescription>
        <dimension>
            <length>0.0</length>
            <width>0.0</width>
            <height>0.0</height>
            <units>Inch</units>
        </dimension>
        <itemWeight>
            <weight>5.0</weight>
            <units>Pound</units>
        </itemWeight>
        <cycleCount>true</cycleCount>
        <purchaseCost>0.0</purchaseCost>
        <unitPrice>1.0</unitPrice>
        <bornOnDateRequired>false</bornOnDateRequired>
        <expirationDateRequired>true</expirationDateRequired>
        <receiveDateRequired>false</receiveDateRequired>
        <quarantineRequired>false</quarantineRequired>
        <inspectionRequired>false</inspectionRequired>
        <hazmat>false</hazmat>
        <hazmatCode/>
        <inventoryTrackingEnabled>true</inventoryTrackingEnabled>
        <lotTrackingEnabled>true</lotTrackingEnabled>
        <serialTrackingEnabled>false</serialTrackingEnabled>
        <shippable>true</shippable>
        <purchased/>
        <receiveOverTolerance/>
        <receiveUnderTolerance/>
        <cycleCountFrequency>0</cycleCountFrequency>
        <reorderQuantity>1920</reorderQuantity>
        <customFields/>
        <packs>
            <pack>
                <type>Each</type>
                <quantity>1</quantity>
                <weight>5.0</weight>
                <dimension>
                    <length>12.0</length>
                    <width>12.0</width>
                    <height>1.0</height>
                    <units>Inch</units>
                </dimension>
                <customMappings xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            </pack>
        </packs>
        <upcs/>
        <productCategory>Miscellaneous</productCategory>
        <customMappings xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
    </item>
</ns2:items>
';

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,$URL);
curl_setopt($ch, CURLOPT_TIMEOUT, 30); //timeout after 30 seconds
curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_ANY);
curl_setopt($ch, CURLOPT_USERPWD, "$username:$password");

curl_setopt($ch, CURLOPT_POSTFIELDS,"xmlRequest=" . $data);                                                                 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: application/json',                                                                                
    'Content-Length: ' . strlen($data_string))                                                                       
);       
$status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);   //get status code
$result = curl_exec($ch);
print_r($result);
curl_close ($ch);
?>
