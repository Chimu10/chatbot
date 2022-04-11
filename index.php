<?php
  require 'intents.php';

  getUsers();

  ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<table class="table">
        <thead>
        <tr>
            <th>Tag</th>
            <th>Pattern</th>
            <th>Responses</th>
        </tr>
        </thead>
        </tbody>
        <?php foreach ($users as $user): ?>
            <tr>
                <td><?php echo $user['tag'] ?></td>
                <td><?php echo $user['patterns'] ?></td>
                <td><?php echo $user['responses'] ?></td>
            </tr>
            <?php endforeach;; ?>
            </tbody>
            </table>
    
</body>
</html>