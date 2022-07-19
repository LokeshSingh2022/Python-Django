const djangoHash = require('/home/lokeshsingh/Documents/Repos/Python-Django/Practice-Django/Hashing/Crypto_Pbkdef2.js');

const password = 'p@ssw0rd';

djangoHash.hash(password)
  .then(hash => {
    console.log('Password: ', hash);

    djangoHash.verify(password, hash)
      .then(result => {
        console.log('Verify: ', result);
      })
      .catch(err => console.log(err));
  })
  .catch(err => console.log(err));