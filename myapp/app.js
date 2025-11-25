var express = require('express');
var app = express();

app.get('/', function (req, res) {
    const fruits = [
        { name: 'Lan', age: 29 },
        { name: 'Bình', age: 35 },
        { name: 'Ngọc', age: 18 },
        { name: 'An', age: 41 },
        { name: 'Hải', age: 22 },
        { name: 'Dương', age: 30 },
        { name: 'Quang', age: 45 },
        { name: 'Cường', age: 27 },
        { name: 'Minh', age: 33 },
        { name: 'Thu', age: 19 }, 
        { name: 'Cường', age: 22 },
        { name: 'Minh', age: 35 },
        { name: 'Thu', age: 12 },
        { name: 'Minh', age: 35 },
        { name: 'Thu', age: 12 },
        { name: 'Cường', age: 22 },
        { name: 'Minh', age: 35 },
        { name: 'Thu', age: 12 },
        { name: 'Minh', age: 35 },
        { name: 'Thu', age: 12 }
    ];
    const testReduce = fruits.reduce((acc, fruit) => {
        fruit.total = acc[fruit.name] ? acc[fruit.name].total + 1 : 0;
        fruit.total
        return acc.push(fruit);
    }, []);
    res.send(testReduce);
});
app.get('/block', function (req, res) {
    res.send('block');
});

app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});

