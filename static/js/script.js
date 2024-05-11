// Get all dropdown items
var dropdownItems = document.querySelectorAll('.dropdown-item');

// Add click event listener to each dropdown item
dropdownItems.forEach(function(item) {
    item.addEventListener('click', function() {
        // Get the text content of the clicked dropdown item
        var department = this.textContent.trim();
        
        // Set the value of the input field to the selected department
        document.getElementById('dept').value = department;
    });
});
