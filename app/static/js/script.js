// Common JavaScript functions for Student Information System

$(document).ready(function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        $('.alert').alert('close');
    }, 5000);

    // Add loading state to buttons when clicked
    $('button[type="submit"], .btn-primary').on('click', function() {
        var $btn = $(this);
        var originalText = $btn.text();
        
        if (!$btn.hasClass('loading')) {
            $btn.addClass('loading');
            $btn.html('<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Loading...');
            
            // Reset button after 3 seconds if no response
            setTimeout(function() {
                if ($btn.hasClass('loading')) {
                    $btn.removeClass('loading');
                    $btn.text(originalText);
                }
            }, 3000);
        }
    });

    // Remove loading state when modal is hidden
    $('.modal').on('hidden.bs.modal', function() {
        $(this).find('button.loading').removeClass('loading').each(function() {
            var $btn = $(this);
            var originalText = $btn.data('original-text') || 'Save';
            $btn.text(originalText);
        });
    });

    // Store original button text
    $('button[type="submit"], .btn-primary').each(function() {
        $(this).data('original-text', $(this).text());
    });

    // Form validation enhancement
    $('form').on('submit', function(e) {
        var $form = $(this);
        var isValid = true;

        // Check required fields
        $form.find('[required]').each(function() {
            var $field = $(this);
            if (!$field.val().trim()) {
                $field.addClass('is-invalid');
                isValid = false;
            } else {
                $field.removeClass('is-invalid');
            }
        });

        if (!isValid) {
            e.preventDefault();
            showAlert('Please fill in all required fields.', 'danger');
        }
    });

    // Remove validation styling when user starts typing
    $('input, select, textarea').on('input change', function() {
        $(this).removeClass('is-invalid');
    });

    // Confirm delete actions
    $('[data-confirm]').on('click', function(e) {
        var message = $(this).data('confirm') || 'Are you sure you want to proceed?';
        if (!confirm(message)) {
            e.preventDefault();
            return false;
        }
    });

    // Search functionality for tables
    $('.table-search').on('input', function() {
        var searchTerm = $(this).val().toLowerCase();
        var tableId = $(this).data('table');
        var $table = $('#' + tableId);
        
        $table.find('tbody tr').each(function() {
            var $row = $(this);
            var text = $row.text().toLowerCase();
            
            if (text.includes(searchTerm)) {
                $row.show();
            } else {
                $row.hide();
            }
        });
    });

    // Responsive table wrapper
    $('.table-responsive').each(function() {
        var $table = $(this);
        var $tableElement = $table.find('table');
        
        if ($tableElement.width() > $table.width()) {
            $table.addClass('has-horizontal-scroll');
        }
    });

    // Smooth scrolling for anchor links
    $('a[href^="#"]').on('click', function(e) {
        var target = $(this.getAttribute('href'));
        if (target.length) {
            e.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 70
            }, 1000);
        }
    });

    // Auto-resize textareas
    $('textarea').on('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });

    // Initialize textarea heights
    $('textarea').each(function() {
        $(this).trigger('input');
    });
});

// Global utility functions
window.SISUtils = {
    // Show alert message
    showAlert: function(message, type = 'info', duration = 5000) {
        var alertClass = 'alert-' + type;
        var alertHtml = `
            <div class="alert ${alertClass} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `;
        
        $('main').prepend(alertHtml);
        
        setTimeout(function() {
            $('.alert').alert('close');
        }, duration);
    },

    // Format date
    formatDate: function(dateString) {
        var date = new Date(dateString);
        return date.toLocaleDateString();
    },

    // Format currency
    formatCurrency: function(amount) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(amount);
    },

    // Debounce function
    debounce: function(func, wait, immediate) {
        var timeout;
        return function executedFunction() {
            var context = this;
            var args = arguments;
            var later = function() {
                timeout = null;
                if (!immediate) func.apply(context, args);
            };
            var callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func.apply(context, args);
        };
    },

    // Throttle function
    throttle: function(func, limit) {
        var inThrottle;
        return function() {
            var args = arguments;
            var context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },

    // Validate email
    isValidEmail: function(email) {
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    },

    // Validate phone number
    isValidPhone: function(phone) {
        var phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
        return phoneRegex.test(phone.replace(/[\s\-\(\)]/g, ''));
    },

    // Copy to clipboard
    copyToClipboard: function(text) {
        if (navigator.clipboard) {
            navigator.clipboard.writeText(text).then(function() {
                SISUtils.showAlert('Copied to clipboard!', 'success', 2000);
            });
        } else {
            // Fallback for older browsers
            var textArea = document.createElement('textarea');
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            SISUtils.showAlert('Copied to clipboard!', 'success', 2000);
        }
    },

    // Download file
    downloadFile: function(data, filename, type = 'text/plain') {
        var blob = new Blob([data], { type: type });
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    },

    // Export table to CSV
    exportTableToCSV: function(tableId, filename) {
        var table = document.getElementById(tableId);
        var rows = table.querySelectorAll('tr');
        var csv = [];
        
        for (var i = 0; i < rows.length; i++) {
            var row = [];
            var cols = rows[i].querySelectorAll('td, th');
            
            for (var j = 0; j < cols.length; j++) {
                var text = cols[j].innerText.replace(/"/g, '""');
                row.push('"' + text + '"');
            }
            
            csv.push(row.join(','));
        }
        
        var csvContent = csv.join('\n');
        SISUtils.downloadFile(csvContent, filename, 'text/csv');
    }
};

// Global error handler
window.addEventListener('error', function(e) {
    console.error('Global error:', e.error);
    SISUtils.showAlert('An error occurred. Please try again.', 'danger');
});

// AJAX error handler
$(document).ajaxError(function(event, xhr, settings, error) {
    console.error('AJAX error:', error);
    if (xhr.status === 0) {
        SISUtils.showAlert('Network error. Please check your connection.', 'danger');
    } else if (xhr.status === 500) {
        SISUtils.showAlert('Server error. Please try again later.', 'danger');
    } else if (xhr.status === 404) {
        SISUtils.showAlert('Resource not found.', 'warning');
    } else {
        SISUtils.showAlert('An error occurred. Please try again.', 'danger');
    }
});
