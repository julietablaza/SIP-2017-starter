var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  var password = document.getElementById("pw").value.toLowerCase(); /* gets user's password input */

  var matchFound = false;
  var searchDone = false;
  var i = 0;

  /* first check for normal words (all letters, no symbols or numbers) */
while (!searchDone && i < wordsList.length) {
    if (wordsList[i].indexOf(password) != -1) {
      matchFound = true;
      searchDone = true;
    }
    i += 1;
  }

  var isBadPwd = matchFound;

  if (isBadPwd == true) {
    document.getElementById("results").innerHTML = "Your password is very weak. Do not use simple words with no characters.";
  } else {
    document.getElementById("results").innerHTML = "other"
  }



}
