const HashPass = require('/home/lokeshsingh/Documents/Repos/Python-Django/Practice-Django/Hashing/Final_Hashing/Encryption_pbkdf2.js')


const password = 'password_12345'
const HashedPass = HashPass.hashPassword(password)
console.log("Password:- " + HashedPass)

console.log("Result:- " + HashPass.verifyPassword(password,HashedPass))