from project3.influencers.base_influencer import BaseInfluencer
from project3.campaigns.base_campaign import BaseCampaign


class StandardInfluencer(BaseInfluencer):
    initial_payment_percentage = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return campaign.budget * self.initial_payment_percentage

    def reached_followers(self, campaign_type: str) -> int:
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.2)
        elif campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.9)