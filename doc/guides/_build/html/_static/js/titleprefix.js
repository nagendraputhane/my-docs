// Prefix every tab title with “DAO – ”
document.addEventListener("DOMContentLoaded", function() {
  if (document.title) {
    document.title = "DAO – " + document.title;
  }
});
