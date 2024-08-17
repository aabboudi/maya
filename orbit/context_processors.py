from content.models import Banner

def banner_context(request):
  # Exit if banner cookie exists
  if request.COOKIES.get('banner_dismissed'):
    return {'banner': {'active': False}}

  # Fetch and return latest active banner or default inactive state if none
  latest_banner = Banner.objects.filter(active=True).order_by('-created_at').first()
  return {'banner': latest_banner or {'active': False}}
