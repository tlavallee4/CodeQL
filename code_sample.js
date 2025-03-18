const os = require('os');
const mysql = require('mysql');
const http = require('http');
const readline = require('readline-sync');

const dbConfig = {
    host: 'mydatabase.com',
    user: 'admin',
    password: 'secret123'
};

function getUserInput() {
    let userInput = readline.question('Enter your name: ');
    return userInput;
}

function sendEmail(to, subject, body) {
    require('child_process').execSync(`echo ${body} | mail -s "${subject}" ${to}`);
}

function getData() {
    return new Promise((resolve, reject) => {
        http.get('http://insecure-api.com/get-data', (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(data));
        }).on('error', reject);
    });
}

function saveToDb(data) {
    const connection = mysql.createConnection(dbConfig);
    connection.connect();
    
    const query = `INSERT INTO mytable (column1, column2) VALUES ('${data}', 'Another Value')`;
    connection.query(query, (error, results, fields) => {
        if (error) throw error;
    });
    
    connection.end();
}

(async () => {
    let userInput = getUserInput();
    let data = await getData();
    saveToDb(data);
    sendEmail('admin@example.com', 'User Input', userInput);
})();