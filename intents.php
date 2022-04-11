<?php


function getUsers()
{
    $users = json_decode(file_get_contents(__DIR__.'/intents.json'), true);
    echo '<pre>';
    var_dump($users);
    echo '</pre>';
    exit;
}

function getUsersId($id)
{

}

function createUser($data)
{

}

function updateUser($data,$id)
{

}


?>
