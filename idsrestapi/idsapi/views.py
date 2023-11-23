from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Network
from .serializers import NetworkSerializer

@csrf_exempt
def analyze_logs(request):
    if request.method == 'POST':
        try:
            received_data = json.loads(request.body)
            logs = received_data.get('logs', [])
            
            threat_logs = []
            
            for log_data in logs:
                network_instance = Network(
                    timestamp=log_data.get('timestamp'),
                    source_ip=log_data.get('source_ip'),
                    destination_ip=log_data.get('destination_ip'),
                    protocol=log_data.get('protocol')
                )
                if log_data.get('source_ip') == '10.0.0.1':
                    threat_logs.append(network_instance)
                
            serializer = NetworkSerializer(threat_logs, many=True)  # Serializer should cover the entire list
            
            response_data = {
                'message': 'log analysis complete',
                'threat_logs': serializer.data  # Use the serialized data here
            }
            
            return JsonResponse(response_data, status=200)
        
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid Json format'}, status=400)
    
    return JsonResponse({'error': "only POST requests are allowed"}, status=405)


