const crypto = require('crypto')


module.exports = {

    keyLength: 32,
    hashAlg: 'sha256',
    iterations: 320000,


    hashPassword(plainText) {
        let salt = crypto.randomBytes(32).toString('base64')
        let pbkdf2 = crypto.pbkdf2Sync(
            plainText,
            salt,
            this.iterations,
            this.keyLength,
            this.hashAlg
        ).toString('base64')
        
        return `${"pbkdf2"}$${this.hashAlg}$${this.keyLength}$${this.iterations}$${salt}$${pbkdf2}`
    },
   
    verifyPassword(givenPassword, hashedPassword) {
        let splits = hashedPassword.split('$')
        
        let hashAlg = splits[1]
        let keyLength = parseInt(splits[2])
        let iterations = parseInt(splits[3])
        let salt = splits[4]
        let pbkdf2 = splits[5]

        let testPbkdf2 = crypto.pbkdf2Sync(
            givenPassword,
            salt,
            iterations,
            keyLength,
            hashAlg
        ).toString('base64')

        return testPbkdf2 === pbkdf2
    },

}