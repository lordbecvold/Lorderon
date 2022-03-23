//Lorderon Client Binary Dev by Lordbecvold
#pragma once

class IEvent
{
	public:
		IEvent();
		~IEvent();
		virtual void	Run() = 0;
		void			SetStartTime(float fTime)	{ m_fStartTime = fTime;	}
		float			GetStartTime()				{ return m_fStartTime;	}

	protected:
		float			m_fStartTime;
};

