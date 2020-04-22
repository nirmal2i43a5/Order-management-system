$(document).ready(() => {
    const searchForm = $(".search-form");
    const searchInput = searchForm.find("[name='name']");
    let typingTimer;
    const typingInterval = 500;
    const searchBtn = searchForm.find("[type='submit']");
  
    searchInput.keyup(event => {
      clearTimeout(typingTimer);
      typingTimer = setTimeout(performSearch, typingInterval);
    });
  
    searchInput.keydown(event => {
      clearTimeout(typingTimer);
    });
  
    function displaySearching() {
      searchBtn.addClass("disabled");
      searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching...");
    }
  
    function performSearch() {
      displaySearching();
      setTimeout(() => {
        let query = searchInput.val();
        window.location.href = `/products/list/?name=${query}`;
      }, 1000)
    }
  });
  