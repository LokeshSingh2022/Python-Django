const crypto = require('crypto')

    const pass = "12345_Hashing"
    const keyLength = 32
    const hashAlg = 'sha256'
    const iterations =  320000


    var hashPassword = function(plainText) {
        let salt = crypto.randomBytes(32).toString('base64')
        let pbkdf2 = crypto.pbkdf2Sync(
            plainText,
            salt,
            iterations,
            keyLength,
            hashAlg
        ).toString('base64')
        
        return `${"pbkdf2_sha256"}$${iterations}$${salt}$${pbkdf2}`
    }
   
    var verifyPassword = function(givenPassword, hashedPassword) {
        let splits = hashedPassword.split('$')
        
        let hashAlg = 'sha256'
        let keyLength = 32
        let iterations = parseInt(splits[1])
        let salt = splits[2]
        let pbkdf2 = splits[3]

        let testPbkdf2 = crypto.pbkdf2Sync(
            givenPassword,
            salt,
            iterations,
            keyLength,
            hashAlg
        ).toString('base64')

        return testPbkdf2 === pbkdf2
    }

console.log("Hashed Password:- " + hashPassword(pass));

console.log("Result is:- " + verifyPassword(pass, hashPassword(pass)))