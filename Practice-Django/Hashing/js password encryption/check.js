var pbkdf2 = require("pbkdf2");

const password = "password_12345";

//const djangoPassword ="pbkdf2_sha256$320000$EkAhjshyeYYPvI3z9r12AB$KVvNP2lMpgx//MxJASzlwqJ5WrtdwnNxZaoYH3ybPMA=";

const djangoPassword2 ="pbkdf2_sha256$320000$IgJL2QV+FxLFxQm5tvTafVF14lYWVan6bttkEhiJuCY=$wHyunpK6GyOR+XxZNW0Hk/T+Vl992BkWwJcx5m5CXag="

var validatePassword = function(key, string) {
  var parts = string.split("$");
  var iterations = parts[1];
  var salt = parts[2];
  const hashPassword = pbkdf2
    .pbkdf2Sync(key, Buffer.from(salt), Number(iterations), 32, "sha256")
    .toString("base64");

  console.log(`parts == ${parts}`)
  console.log(`iterations == ${iterations}`)
  console.log(`salt == ${salt}`)
  console.log(`hashPassword == ${hashPassword}`)

  return hashPassword === parts[3];
};

console.log(validatePassword(password, djangoPassword2));

//a5fcec9ebb0c158254463e
//FbaZqRTtEUEVljgkwWDUPg==
//SA7IXkI8kwwDucy09++8ilhD8pdb1MwvDuvGJ7wMq6Y=