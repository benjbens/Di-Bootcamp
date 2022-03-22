
let sen = `The moovie is not that bad, I like it`;
let arr = sen.split(` `)

let not = arr.indexOf(`not`);
let bad = arr.indexOf(`bad`);
arr.splice(not,bad-not+3,`good`);
console.log(arr.join(` `));