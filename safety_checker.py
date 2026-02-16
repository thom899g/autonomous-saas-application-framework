from typing import Dict, Optional
import logging

class SafetyChecker:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def check_compliance(self, app_data: Dict) -> Dict:
        """Ensures the application meets safety and ethical standards."""
        try:
            # Simulated compliance checks
            issues = []
            
            if 'terms' not in app_data or 'privacy policy' not in app_data:
                issues.append("Missing legal documents")
                
            if app_data['type'] == 'AI Analysis':
                issues.extend(self._check_ai_ethics(app_data))
                
            result = {
                'is_compliant': len(issues) == 0,
                'violations': issues
            }
            
            return result
            
        except Exception as e:
            self.logger.error(f"Compliance check failed: {str(e)}")
            raise

    def _check_ai_ethics(self, app_data: Dict) -> list:
        """Checks AI-related ethical violations."""
        issues = []
        
        if 'data sources' not in app_data or len(app_data['data sources']) == 0:
            issues.append("Missing data sources declaration")
            
        return issues