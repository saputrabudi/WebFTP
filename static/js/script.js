// WebFTP JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Animasikan flash messages
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 5000);
    });

    // Tooltip initialization
    const tooltipTriggerList = [].slice.call(
        document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Konfirmasi untuk delete action
    const deleteButtons = document.querySelectorAll('[data-confirm]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm(this.dataset.confirm)) {
                e.preventDefault();
            }
        });
    });
    
    // Responsive table handling
    const adjustTableForMobile = () => {
        if (window.innerWidth < 768) {
            const tables = document.querySelectorAll('.table-responsive table');
            tables.forEach(table => {
                const actionCols = table.querySelectorAll('th:last-child, td:last-child');
                actionCols.forEach(col => {
                    col.style.width = 'auto';
                });
            });
        }
    };
    
    window.addEventListener('resize', adjustTableForMobile);
    adjustTableForMobile();
    
    // Highlight current path in breadcrumb
    const breadcrumbItems = document.querySelectorAll('.breadcrumb-item');
    if (breadcrumbItems.length > 0) {
        breadcrumbItems[breadcrumbItems.length - 1].classList.add('active');
    }
    
    // Add event listeners to file/directory rows for easier click
    const fileRows = document.querySelectorAll('tr[data-href]');
    fileRows.forEach(row => {
        row.addEventListener('click', function(e) {
            if (e.target.tagName.toLowerCase() !== 'a' && e.target.tagName.toLowerCase() !== 'button') {
                window.location.href = this.dataset.href;
            }
        });
        
        // Menambahkan style pointer untuk menunjukkan bahwa baris dapat diklik
        row.style.cursor = 'pointer';
    });
}); 