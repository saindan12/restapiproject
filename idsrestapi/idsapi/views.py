from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Network

@csrf_exempt
def analyze_logs(request):
    if request.method == 'POSt':
        try:
            received_data = json.loads(request.body)
            logs = received_data.get('logs',[])
            
            threat_logs = []
            
            for log_data in logs:
                if log_data.get('source_ip') == '10.0.0.1':
                    threat_logs.append(log_data)
                    
            response_data ={
                'message': 'log analysis complete',
                'threat_logs' : threat_logs
            }
            
            return JsonResponse(response_data, status=200)
        
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid Json format'}, status=400)
    
    return JsonResponse({'error': "only POST requests are allowed"}, status=405)


