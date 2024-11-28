from project3.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    low_budget_campaign = 2500.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.low_budget_campaign, required_engagement)

    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= self.required_engagement * 0.9