var fs = require("fs");

var charset = [...Array(126-33-1)].map((_,i)=>String.fromCharCode(i+33));
console.log(charset.join(""));
var passwords = [];

for(var i1 of charset){
if(i1==="0")break;

for(var i2 of charset)
for(var i3 of charset){
	for(var i4 of charset)
	for(var i5 of charset)
		passwords.push(i1+i2+i3+i4+i5);

	var content = passwords.join("\n");
	passwords = [];
	fs.appendFileSync(i1.charCodeAt(0)+".txt", content);
}
console.log(i1);
}
