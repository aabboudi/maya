function copyUrlToClipboard() {
  (async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);

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
