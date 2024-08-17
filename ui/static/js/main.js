function copyUrlToClipboard() {
  (async () => {
    try {
      // Copy current URL to clipboard
      await navigator.clipboard.writeText(window.location.href);

      // Discard toast notification after 5 seconds
      const toast = document.getElementById('dismiss-toast');
      if (toast) {
        toast.classList.remove('hidden');
        setTimeout(() => {
          toast.classList.add('hidden');
        }, 5000);
      }
    } catch (error) {
      console.error('Failed to copy URL to clipboard', error);
    }
  })();
}

function handleBannerCookie() {
  // Check if banner cookie exists
  if (document.cookie.split(';').some((item) => item.trim().startsWith('banner_dismissed='))) {
    document.getElementById('ab-full-width-with-dismiss-button-on-blue-bg').style.display = 'none';
  }

  // Set cookie when banner is dismissed
  document.getElementById('dismiss-banner').addEventListener('click', function () {
    document.cookie = "banner_dismissed=true; path=/; max-age=86400"; // 24*60*60
    document.getElementById('ab-full-width-with-dismiss-button-on-blue-bg').style.display = 'none';
  });
}
