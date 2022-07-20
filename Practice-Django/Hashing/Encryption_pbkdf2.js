const crypto = require('crypto')

module.exports = {

    keyLength: 32,
    hashAlg: 'sha256',
    iterations: 320000,

    randHex(length) {
        return crypto.randomBytes(length / 2).toString('hex')
    },

    hashPassword(plainText) {
        let salt = this.randHex(64)
        let pbkdf2 = crypto.pbkdf2Sync(
            plainText,
            salt,
            this.this.iterations,
            this.keyLength,
            this.hashAlg
        ).toString('hex')

        return `${pbkdf2}:${this.hashAlg}:${this.keyLength}:${this.iterations}:${salt}`
    },

    verifyPassword(givenPassword, hashedPassword) {
        let splits = hashedPassword.split(':')
        let hashAlg = splits[0]
        let keyLength = parseInt(splits[1])
        let iterations = parseInt(splits[2])
        let salt = splits[3]
        let pbkdf2 = splits[4]

        let testPbkdf2 = crypto.pbkdf2Sync(
            givenPassword,
            salt,
            this.iterations,
            keyLength,
            hashAlg
        ).toString('hex')

        return testPbkdf2 === pbkdf2
    }

}