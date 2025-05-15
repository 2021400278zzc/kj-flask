from app.modules.sched.member_score_sched import MemberScoreScheduler

def init_schedulers(app):
    
    # 初始化成员得分更新调度器
    member_score_scheduler = MemberScoreScheduler(app)
    
    return {
        'member_score': member_score_scheduler

    }
