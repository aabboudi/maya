from content.models import Banner

def banner_context(request):
  # Fetch and return latest active banner or default inactive state if none
  latest_banner = Banner.objects.filter(active=True).order_by('-created_at').first()
  return {'banner': latest_banner or {'active': False}}
